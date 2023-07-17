import axios from 'axios'

// import { MessageBox, Message } from 'element-ui'
// create an axios instance
const service = axios.create({
    baseURL: process.env.VUE_APP_BASE_API, // url = base url + request url
    withCredentials: true, // send cookies when cross-domain requests
    timeout: 5000 // request timeout
})

// request interceptor
service.interceptors.request.use(
    config => {
        var token = window.sessionStorage.getItem('Authorization')
        if (token) {
          // let each request carry token
          // please modify it according to the actual situation
          config.headers['Authorization'] = 'Bearer ' + token
        }
        return config
    },
    error => {
        // do something with request error
        // console.log('request: ', error) // for debug
        return Promise.reject(error)
    }
)

// response interceptor
service.interceptors.response.use(
    /**
   * If you want to get http information such as headers or status
   * Please return  response => response
  */

    /**
   * Determine the request status by custom code
   * Here is just an example
   * You can also judge the status by HTTP Status Code
   */
    response => {
        const res = response.data
        const status = response.status
        if (status != 200) {
            return Promise.reject(new Error(res.msg || res.message || 'Error'))
        }

        return res
    },
    error => {
        console.log('response:', error) // for debug
        return Promise.reject(error)
    }
)

export default service
