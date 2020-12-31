window.axios = require('axios');

window.axios.defaults.headers.common['x-Requested-With'] = 'XMLHttpRequest'

window.visa = () => {
    let token = null

    let headers = {
        'Accept': 'application/json',
        'content-Type': 'application/json'
    }
    if (token) {
        headers['Authorization'] = 'Bearer' + token
    }
    return { headers }
};