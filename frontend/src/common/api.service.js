import { CSRF_TOKEN } from "./csrf_token.js"
import axios from 'axios'

function handleResponse(response) {
    if (response.status === 204) {
        return ''
    } else if (response.status === 404) {
        return "not found"
    }
    else if (response.status === 403) {
        return "403"
    } else if (response.status === 400){
        // console.log(response.json())
        return "wrong data"
    }
    else if (response.status === 401){
        // console.log(response.json())
        return "gosc"
    }
    else{
        // if(response.url.indexOf('/timeplot') == -1){
            // }
            if(response.headers.get("Content-Type") != "application/json"){
                return response.text()
            }
            return response.json()
    }
}

function apiService(endpoint, method, data) {
    // console.log("url: ", endpoint,
        // "\nmethod: ", method,
        // "\ndata:", data);
    const config = {
        method: method || "GET",
        body: data != undefined ? JSON.stringify(data) : null,
        
        headers: {
            // 'content-type': 'text/html; charset=utf-8
            // ,
            'content-type': 'application/json;',
            'X-CSRFTOKEN': CSRF_TOKEN
        }
    }
    return fetch(endpoint, config)
        .then(handleResponse)
        .catch(error => {console.log(error)})
}

function imageUpload(formData){
    let config = {
    headers: {
        'content-type': 'multipart/form-data;',
        'X-CSRFTOKEN': CSRF_TOKEN
        }
    }

    return axios.post("/api/photo/", formData, config)
    .then(console.log("success"))
    .catch(error => console.log(error));
}

function changeImage(url){
    let config = {
    headers: {
        'Content-Type': 'multipart/form-data;  boundary=--------------------------339261229255605205279691',
        'X-CSRFTOKEN': CSRF_TOKEN
        }
    }

    return axios.put(url, {"name": "cos"}, config)
    .then()
    .catch(error => console.log(error));
}

export { apiService, imageUpload, changeImage }