import http from 'k6/http';
import {sleep} from 'k6';

export const options = {
  // Key configurations for avg load test in this section
  stages: [
    { duration: '2m', target: 1000 }, // traffic ramp-up from 1 to 100 users over 5 minutes.
    { duration: '2m', target: 1000 }, // stay at 100 users for 30 minutes
    { duration: '2m', target: 0 }, // ramp-down to 0 users
  ],
};

export default () => {
    let response = http.get('http://localhost:8000');
    console.log(`Response time: ${response.timings.duration} ms`);
    sleep(1);
}
