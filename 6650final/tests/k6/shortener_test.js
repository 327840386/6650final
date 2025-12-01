import http from 'k6/http';
import { sleep } from 'k6';


export let options = {
vus: 50,
duration: '30s',
};


export default function () {
let payload = JSON.stringify({ url: 'https://example.com' });
let params = { headers: { 'Content-Type': 'application/json' } };
http.post(__ENV.BASE, payload, params);
sleep(0.1);
}