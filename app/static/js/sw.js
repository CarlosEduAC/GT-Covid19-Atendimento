const CACHE_NAME = 'covid-19-app';

self.addEventListener('install', function(event) {
      event.waitUntil(
            caches.open(CACHE_NAME).then(function(cache) {
                  return cache.addAll(
                        [
                            '/',
                            '/primeiroAtendimento',
                            '/static/css/app.css'
                        ]
                  );
            })
      );
});


self.addEventListener('install', function (event) {
    event.waitUntil(self.skipWaiting()); // Activate worker immediately
});

self.addEventListener('activate', function (event) {
    event.waitUntil(self.clients.claim()); // Become available to all pages
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