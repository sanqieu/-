<template>
  <el-form :model="form" label-width="80px" style="max-width:350px;margin:60px auto">
    <el-form-item label="用户名">
      <el-input v-model="form.username"/>
    </el-form-item>
    <el-form-item label="密码">
      <el-input type="password" v-model="form.password"/>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="login">登录</el-button>
      <el-button link @click="toRegister">注册</el-button>
    </el-form-item>
  </el-form>
</template>
<script setup>
import { ref } from 'vue'
import { login } from '../api/user'
import { useRouter } from 'vue-router'
const form = ref({ username:'', password:'' })
const router = useRouter()
async function loginHandler() {
  const res = await login(form.value)
  localStorage.setItem('token', res.data.token)
  router.push('/')
}
function toRegister() {
  router.push('/register')
}
const login = loginHandler
</script>