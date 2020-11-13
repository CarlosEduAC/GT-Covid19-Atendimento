// Names of the two caches used in this version of the service worker.
// Change to v2, etc. when you update any of the local resources, which will
// in turn trigger the install event again.
const PRECACHE = 'precache-v7';
const RUNTIME = 'runtime';

// A list of local resources we always want to be cached.
const PRECACHE_URLS = [
    '/',
    '/primeiroAtendimento',
    '/static/css/app.css'
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
        // Try the cache
        const cachedResponse = await caches.match(event.request);
        if (cachedResponse) return cachedResponse;

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

            // Fall back to network
            return returnResponse;
        } catch (err) {
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
            }
            // If both fail, show a generic fallback:
            return caches.match('/');
            // However, in reality you'd have many different
            // fallbacks, depending on URL & headers.
            // Eg, a fallback silhouette image for avatars.
        }
    }());
});
