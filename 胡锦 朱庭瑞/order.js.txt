import request from './index'

export function createOrder(data) {
  return request.post('order/order/', data)
}

export function getOrderList() {
  return request.get('order/order/')
}

export function getOrderDetail(id) {
  return request.get(`order/order/${id}/`)
}