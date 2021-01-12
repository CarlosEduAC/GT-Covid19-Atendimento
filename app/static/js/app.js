$(document).ready(function () {

    // fetch('/dados').then((response) => {
    //     if (response.ok) {
    //         localStorage.setItem('pacientesDados', JSON.stringify(response.json().data.pacientes));
    //         localStorage.setItem('agendamentos', JSON.stringify(response.json().data.agendamentos));
    //     }
    // });

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

            const getLocalStorageArray = (name) => JSON.parse(localStorage.getItem(name)) ?? [];

            let failedAtendimentosArray = getLocalStorageArray('failedAtendimentos');
            // let pacientesDadosArr = getLocalStorageArray('pacientesDados');
            let agendamentosArr = getLocalStorageArray('agendamentos');

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
                        const newPostCopy = {};

                        $('form').children().find('input').map(function () {
                            Object.assign(newPostCopy, {[$(this).attr('name')]: $(this).val()});
                        });

                        if (Object.keys(newPostCopy).length > 0) {
                            let newPost = {};

                            // Polyfill
                            if (!Date.now) {
                                Date.now = function now() {
                                    return new Date().getTime();
                                };
                            }

                            newPostCopy.failed_at = Date.now();

                            // does specific things for different routes
                            const routeArr = window.location.pathname.split('/').filter((x) => x !== '');

                            if (routeArr.length > 0) {
                                switch (routeArr[0]) {
                                    case 'atendimento':
                                        if (routeArr.length > 1) {

                                            // isso serve para mesclar os dados do paciente que já estão salvos
                                            // com o que será adicionado de novo, além de adicionar o id_inicial
                                            // do agendamento
                                            // const currAgendamento = agendamentosArr.find(x => x.id === routeArr[1]);
                                            // const idPaciente = currAgendamento.idPaciente;
                                            // const atualPacienteDados = pacientesDadosArr.find(x => x.id === idPaciente);

                                            // Object.assign(newPost, atualPacienteDados);
                                            newPost.id_inicial = routeArr[1];

                                        }
                                        break;
                                }
                            }

                            Object.assign(newPost, newPostCopy);

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
