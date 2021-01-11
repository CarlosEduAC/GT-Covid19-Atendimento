// Names of the two caches used in this version of the service worker.
// Change to v2, etc. when you update any of the local resources, which will
// in turn trigger the install event again.
const PRECACHE = 'precache-v2.0';
const RUNTIME = 'runtime-v2.0';

// A list of local resources we always want to be cached.
const PRECACHE_URLS = [
    '/',
    '/primeiroAtendimento',
    '/atendimento/novo',
    '/static/css/app.css',
    '/static/js/axios.min.js'
];

const RUNTIME_URLS = [
    '/'
];

// The install handler takes care of precaching the resources we always need.
self.addEventListener('install', event => {
    event.waitUntil(
        caches.open(PRECACHE)
            .then(cache => cache.addAll(PRECACHE_URLS))
            .then(self.skipWaiting())
    );
});

// The activate handler takes care of cleaning up old caches.
self.addEventListener('activate', event => {
    const currentCaches = [PRECACHE, RUNTIME];
    event.waitUntil(
        caches.keys().then(cacheNames => {
            return cacheNames.filter(cacheName => !currentCaches.includes(cacheName));
        }).then(cachesToDelete => {
            return Promise.all(cachesToDelete.map(cacheToDelete => {
                return caches.delete(cacheToDelete);
            }));
        }).then(() => self.clients.claim())
    );
});

self.addEventListener('fetch', (event) => {
    event.respondWith(async function() {
        try {
            const returnResponse = await fetch(event.request.clone());
            if (event.request.method === 'POST') {
                self.clients.matchAll().then(function(clients) {
                    clients.forEach(function(client) {

                        const message = {
                            message: 'successful-post',
                            url: event.request.url
                        };

                        client.postMessage({ message: JSON.stringify(message) });
                    });
                });
            }

            // isso checa se estamos fazendo uma requisição pra algum ítem que está listado para ser salvo em cache
            // e atualiza o cache nesse caso
            RUNTIME_URLS.map((x) => {
                const url = new URL(event.request.url);
                if (x === url.pathname) {
                    caches.open(RUNTIME)
                        // isso torna as requisições custosas por duplicá-las
                        // mas não encontrei uma alternativa já que é impossível fazer cache.put()
                        // com o clone da resposta
                        .then(cache => cache.addAll([event.request]));
                }
            });

            // Fall back to network
            return returnResponse;
        } catch (err) {
            const url = new URL(event.request.url);

            if (event.request.method === 'POST') {
                self.clients.matchAll().then(function(clients) {
                    clients.forEach(function(client) {

                        const message = {
                            message: 'failed-post',
                            url: event.request.url
                        };

                        client.postMessage({ message: JSON.stringify(message) });
                    });
                });
            } else if (event.request.method === 'GET') {
                const routeArr = url.pathname.split('/').filter((x) => x !== '');

                if (routeArr.length > 0) {
                    switch (routeArr[0]) {
                        case 'atendimento':
                            if (routeArr.length > 1) {
                                return await caches.match('/atendimento/novo');
                            }
                                break;
                        }
                }
            }

            // Try the cache
            const cachedResponse = await caches.match(event.request);
            if (cachedResponse) return cachedResponse;

            // If everything fails, show a generic fallback:
            return caches.match('/');
            // However, in reality you'd have many different
            // fallbacks, depending on URL & headers.
            // Eg, a fallback silhouette image for avatars.
        }
    }());
});
