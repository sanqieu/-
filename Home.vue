<template>
  <div>
    <el-row :gutter="20" style="margin-bottom:20px">
      <el-col :span="6" v-for="dish in dishes" :key="dish.id">
        <el-card :body-style="{padding:'16px'}">
          <img :src="dish.image" alt="" style="width:100%;height:150px;object-fit:cover">
          <div style="margin:10px 0;font-weight:bold">{{ dish.name }}</div>
          <div>￥{{ dish.price }}</div>
          <el-button type="primary" size="small" @click="viewDetail(dish.id)">查看详情</el-button>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>
<script setup>
import { ref, onMounted } from 'vue'
import { getDishList } from '../api/dish'
import { useRouter } from 'vue-router'

const dishes = ref([])
const router = useRouter()
onMounted(async () => {
  const res = await getDishList()
  dishes.value = res.data
})
function viewDetail(id) {
  router.push(`/dish/${id}`)
}
</script>