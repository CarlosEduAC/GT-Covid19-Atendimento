$(document).ready(function () {

    const syncError = () => Swal.fire({
        title: 'Ops!',
        text: 'Não foi possível sincronizar. Talvez você não possua conexão com a internet... :(',
        icon: 'error',
        confirmButtonText: 'Ok'
    });

    if ('serviceWorker' in navigator) {
        // we are checking here to see if the browser supports the  service worker api
        navigator.serviceWorker.register('/sw.js', { scope: '/' })
            .catch(function (err) {
                    // sw registration failed :(
                    console.log('ServiceWorker registration failed: ', err);
                }
            );

        navigator.serviceWorker.addEventListener('message', event => {
            const eventMessage = JSON.parse(event.data.message);
            const urlString = eventMessage.url;
            const url = new URL(urlString);

            const getFailedAtendimentosArray = () => JSON.parse(localStorage.getItem('failedAtendimentos')) ?? [];

            let failedAtendimentosArray = getFailedAtendimentosArray();

            function deleteItem(index) {
                failedAtendimentosArray.splice(index, 1);
                localStorage.setItem('failedAtendimentos', JSON.stringify(failedAtendimentosArray));
            }

            switch(eventMessage.message) {
                case 'successful-post':
                    if (url.searchParams.get('sync')) {
                        const index = url.searchParams.get('index');

                        deleteItem(index);

                        if (
                            !url.searchParams.get('batch')
                            || (url.searchParams.get('batch') && url.searchParams.get('batch_end'))
                        ) {

                            document.location.replace('/');
                        }
                    }
                    break;
                case 'failed-post':
                    syncError();
                    if (!url.searchParams.get('sync')) {
                        // stores every input name-value information at an object
                        const newPost = {};

                        $('form').children().find('input').map(function () {
                            Object.assign(newPost, {[$(this).attr('name')]: $(this).val()});
                        });

                        // Polyfill
                        if (!Date.now) {
                            Date.now = function now() {
                                return new Date().getTime();
                            };
                        }

                        if (Object.keys(newPost).length > 0) {
                            newPost.failed_at = Date.now();

                            // gets the array of failed atendimentos if exists
                            let failedAtendimentosArray = JSON.parse(localStorage.getItem('failedAtendimentos'));

                            // makes it an array if there are no failed atendimentos
                            if (!failedAtendimentosArray) {
                                failedAtendimentosArray = [];
                            }

                            failedAtendimentosArray.push(newPost);

                            // stores the new post at the browser's localStorage
                            localStorage.setItem('failedAtendimentos', JSON.stringify(failedAtendimentosArray));
                            console.log(`POST Request falhou: `, failedAtendimentosArray, 'Salvo no localStorage.');
                        }
                    }
                    break;
            }
        });

    }

});
