<template>
  <el-row>
    <el-col :span="10">
      <img :src="dish.image" style="width:100%;height:250px;object-fit:cover">
    </el-col>
    <el-col :span="14" style="padding-left:32px">
      <h2>{{ dish.name }}</h2>
      <div>分类：{{ dish.category }}</div>
      <div style="margin:10px 0">
        <span v-for="tag in dish.tags" :key="tag" class="tag">{{ tag }}</span>
      </div>
      <div>￥{{ dish.price }}</div>
      <div style="margin:12px 0">{{ dish.description }}</div>
      <el-input-number v-model="count" :min="1" />
      <el-button type="primary" @click="add">加入购物车</el-button>
    </el-col>
  </el-row>
</template>
<script setup>
import { ref, onMounted } from 'vue'
import { getDishDetail } from '../api/dish'
import { useRoute } from 'vue-router'
import { useCartStore } from '../store/cart'
const dish = ref({})
const route = useRoute()
const cart = useCartStore()
const count = ref(1)
onMounted(async () => {
  const res = await getDishDetail(route.params.id)
  dish.value = res.data
})
function add() {
  cart.addToCart(dish.value, count.value)
}
</script>
<style scoped>
.tag { margin-right:8px;background:#f2f2f2;padding:2px 6px;border-radius:4px }
</style>