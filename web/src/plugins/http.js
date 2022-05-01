import Vue from 'vue'
import axios from 'axios'


export default {
    install: function (Vue, options) {
        const http = axios.create({
            baseURL: 'http://localhost:8000/'
        })
        Vue.prototype.$axios = http
    }
}
