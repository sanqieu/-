<template>
  <div>
    <el-card>
      <h2>个人信息</h2>
      <div>用户名：{{ user.username }}</div>
      <div>手机号：{{ user.phone }}</div>
      <div>地址：{{ user.address }}</div>
    </el-card>
  </div>
</template>
<script setup>
import { ref, onMounted } from 'vue'
import { getUserInfo } from '../api/user'
const user = ref({})
onMounted(async () => {
  const res = await getUserInfo()
  user.value = res.data
})
</script>