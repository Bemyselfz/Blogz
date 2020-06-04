import axios from 'axios'

export function request (config, ) {
  return new Promise((resolve, reject) => {
    const axiosIns1 = axios.create({
      // baseURL: 'http://127.0.0.1:8000/api',
      baseURL: 'http://www.ineed520.cn/api',
    })

    // 发送网络请求
    axiosIns1(config)
      .then(res => {
        resolve(res)
      })
      .catch(err => {
        reject(err)
      })
  })

}