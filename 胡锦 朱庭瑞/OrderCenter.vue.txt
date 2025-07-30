<template>
  <div>
    <h2>购物车</h2>
    <el-table :data="cart.items" style="width:100%">
      <el-table-column prop="dish.name" label="菜品"></el-table-column>
      <el-table-column prop="dish.price" label="单价"></el-table-column>
      <el-table-column prop="quantity" label="数量"></el-table-column>
      <el-table-column label="操作">
        <template #default="scope">
          <el-button size="small" type="danger" @click="remove(scope.row.dish.id)">移除</el-button>
        </template>
      </el-table-column>
    </el-table>
    <div style="margin:16px 0">总价：￥{{ total }}</div>
    <el-button type="primary" @click="submitOrder" :disabled="cart.items.length==0">提交订单</el-button>
    <el-divider></el-divider>
    <h2>历史订单</h2>
    <el-table :data="orders" style="width:100%">
      <el-table-column prop="id" label="订单号"></el-table-column>
      <el-table-column prop="total_price" label="总价"></el-table-column>
      <el-table-column prop="status" label="状态"></el-table-column>
      <el-table-column prop="created_at" label="下单时间"></el-table-column>
    </el-table>
  </div>
</template>
<script setup>
import { ref, computed, onMounted } from 'vue'
import { useCartStore } from '../store/cart'
import { createOrder, getOrderList } from '../api/order'

const cart = useCartStore()
const total = computed(() => cart.items.reduce((sum, i) => sum + i.dish.price * i.quantity, 0))
const orders = ref([])

function remove(id) {
  cart.removeFromCart(id)
}
async function submitOrder() {
  const orderData = {
    items: cart.items.map(i => ({ dish: i.dish.id, quantity: i.quantity })),
    total_price: total.value,
    address: '默认地址'
  }
  await createOrder(orderData)
  cart.clearCart()
  fetchOrders()
}
async function fetchOrders() {
  const res = await getOrderList()
  orders.value = res.data
}
onMounted(() => {
  fetchOrders()
})
</script>