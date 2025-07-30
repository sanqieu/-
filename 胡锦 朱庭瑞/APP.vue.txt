<template>
  <el-container style="min-height:100vh">
    <el-header>
      <el-menu :router="true" mode="horizontal" background-color="#409EFF" text-color="#fff" active-text-color="#ffd04b">
        <el-menu-item index="/">首页</el-menu-item>
        <el-menu-item index="/order">订单中心</el-menu-item>
        <el-menu-item index="/user">用户中心</el-menu-item>
      </el-menu>
    </el-header>
    <el-main>
      <router-view></router-view>
    </el-main>
  </el-container>
</template>