<template>
  <div>
    <h1 class="text-h4 mb-6">用户管理</h1>

    <v-card>
      <v-data-table
        :headers="headers"
        :items="users"
        :loading="loading"
        class="elevation-1"
      >
        <template v-slot:item.role="{ item }">
          <v-chip :color="item.role === 'admin' ? 'error' : 'primary'" small>
            {{ item.role === 'admin' ? '管理员' : '普通用户' }}
          </v-chip>
        </template>

        <template v-slot:item.created_at="{ item }">
          {{ formatDate(item.created_at) }}
        </template>

        <template v-slot:item.actions="{ item }">
          <v-btn
            size="small"
            :color="item.role === 'admin' ? 'primary' : 'error'"
            @click="toggleRole(item)"
          >
            {{ item.role === 'admin' ? '设为普通用户' : '设为管理员' }}
          </v-btn>
        </template>
      </v-data-table>
    </v-card>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const loading = ref(false)
const users = ref([])

const headers = [
  { title: 'ID', key: 'id', align: 'start' },
  { title: '用户名', key: 'username', align: 'start' },
  { title: '邮箱', key: 'email', align: 'start' },
  { title: '角色', key: 'role', align: 'center' },
  { title: '注册时间', key: 'created_at', align: 'center' },
  { title: '操作', key: 'actions', align: 'center', sortable: false }
]

const formatDate = (date) => {
  return new Date(date).toLocaleDateString('zh-CN')
}

const toggleRole = async (user) => {
  // TODO: 调用API切换角色
  console.log('切换用户角色:', user.id)
}

onMounted(async () => {
  loading.value = true
  // TODO: 从API获取用户列表
  setTimeout(() => {
    users.value = []
    loading.value = false
  }, 500)
})
</script>
