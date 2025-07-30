import request from './index'

export function getDishList(params = {}) {
  return request.get('food/dish/', { params })
}

export function getDishDetail(id) {
  return request.get(`food/dish/${id}/`)
}

export function getCategoryList() {
  return request.get('food/category/')
}