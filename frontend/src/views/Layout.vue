<template>
  <v-app>
    <!-- 侧边栏 -->
    <v-navigation-drawer v-model="drawer" app>
      <v-list-item class="pa-4">
        <v-list-item-title class="text-h6">
          文章管理系统
        </v-list-item-title>
        <v-list-item-subtitle>
          {{ authStore.user?.username }}
        </v-list-item-subtitle>
      </v-list-item>

      <v-divider></v-divider>

      <v-list dense nav>
        <v-list-item
          v-for="item in menuItems"
          :key="item.path"
          :to="item.path"
          :prepend-icon="item.icon"
          :title="item.title"
          :value="item.path"
        ></v-list-item>
      </v-list>
    </v-navigation-drawer>

    <!-- 顶部栏 -->
    <v-app-bar app color="primary" dark>
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title>{{ pageTitle }}</v-toolbar-title>
      <v-spacer></v-spacer>

      <v-menu>
        <template v-slot:activator="{ props }">
          <v-btn icon v-bind="props">
            <v-icon>mdi-account-circle</v-icon>
          </v-btn>
        </template>
        <v-list>
          <v-list-item>
            <v-list-item-title>{{ authStore.user?.email }}</v-list-item-title>
            <v-list-item-subtitle>{{ authStore.isAdmin ? '管理员' : '普通用户' }}</v-list-item-subtitle>
          </v-list-item>
          <v-divider></v-divider>
          <v-list-item @click="handleLogout">
            <v-list-item-title>
              <v-icon>mdi-logout</v-icon>
              退出登录
            </v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
    </v-app-bar>

    <!-- 主内容区 -->
    <v-main>
      <v-container fluid>
        <router-view></router-view>
      </v-container>
    </v-main>
  </v-app>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const router = useRouter()
const route = useRoute()
const authStore = useAuthStore()

const drawer = ref(true)

const menuItems = computed(() => {
  const items = [
    { path: '/dashboard', title: '工作台', icon: 'mdi-view-dashboard' },
    { path: '/articles', title: '文章管理', icon: 'mdi-file-document-multiple' },
    { path: '/configs', title: '配置管理', icon: 'mdi-cog' },
    { path: '/ai-models', title: 'AI模型配置', icon: 'mdi-brain' }
  ]

  if (authStore.isAdmin) {
    items.push({ path: '/users', title: '用户管理', icon: 'mdi-account-group' })
  }

  return items
})

const pageTitle = computed(() => {
  const item = menuItems.value.find(item => route.path.startsWith(item.path))
  return item?.title || '文章管理系统'
})

const handleLogout = () => {
  authStore.logout()
  router.push('/login')
}
</script>
