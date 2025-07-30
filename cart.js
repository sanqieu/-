import { defineStore } from 'pinia'

export const useCartStore = defineStore('cart', {
  state: () => ({
    items: []
  }),
  actions: {
    addToCart(dish, quantity = 1) {
      const existing = this.items.find(item => item.dish.id === dish.id)
      if (existing) existing.quantity += quantity
      else this.items.push({ dish, quantity })
    },
    removeFromCart(dishId) {
      this.items = this.items.filter(item => item.dish.id !== dishId)
    },
    clearCart() {
      this.items = []
    }
  }
})