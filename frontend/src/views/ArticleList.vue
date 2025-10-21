<template>
  <div>
    <v-row class="mb-4">
      <v-col cols="12" md="6">
        <h1 class="text-h4">文章管理</h1>
      </v-col>
      <v-col cols="12" md="6" class="text-right">
        <v-btn color="primary" to="/articles/create">
          <v-icon left>mdi-plus</v-icon>
          创建文章
        </v-btn>
      </v-col>
    </v-row>

    <v-card>
      <v-card-title>
        <v-text-field
          v-model="search"
          label="搜索文章"
          prepend-inner-icon="mdi-magnify"
          variant="outlined"
          density="compact"
          hide-details
          clearable
        ></v-text-field>
      </v-card-title>

      <v-data-table
        :headers="headers"
        :items="articles"
        :search="search"
        :loading="loading"
        class="elevation-1"
      >
        <template v-slot:item.created_at="{ item }">
          {{ formatDate(item.created_at) }}
        </template>

        <template v-slot:item.status="{ item }">
          <v-chip :color="getStatusColor(item.status)" small>
            {{ item.status }}
          </v-chip>
        </template>

        <template v-slot:item.actions="{ item }">
          <v-btn
            icon
            size="small"
            @click="viewArticle(item.id)"
          >
            <v-icon>mdi-eye</v-icon>
          </v-btn>
          <v-btn
            icon
            size="small"
            @click="editArticle(item.id)"
          >
            <v-icon>mdi-pencil</v-icon>
          </v-btn>
          <v-btn
            icon
            size="small"
            color="error"
            @click="deleteArticle(item)"
          >
            <v-icon>mdi-delete</v-icon>
          </v-btn>
        </template>
      </v-data-table>
    </v-card>

    <!-- 删除确认对话框 -->
    <v-dialog v-model="deleteDialog" max-width="400">
      <v-card>
        <v-card-title>确认删除</v-card-title>
        <v-card-text>
          确定要删除文章 "{{ deleteTarget?.title }}" 吗？此操作不可恢复。
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn @click="deleteDialog = false">取消</v-btn>
          <v-btn color="error" @click="confirmDelete">删除</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const search = ref('')
const loading = ref(false)
const articles = ref([])
const deleteDialog = ref(false)
const deleteTarget = ref(null)

const headers = [
  { title: '标题', key: 'title', align: 'start' },
  { title: '分类', key: 'category', align: 'start' },
  { title: '状态', key: 'status', align: 'center' },
  { title: '创建时间', key: 'created_at', align: 'center' },
  { title: '操作', key: 'actions', align: 'center', sortable: false }
]

const formatDate = (date) => {
  return new Date(date).toLocaleDateString('zh-CN', {
    year: 'numeric',
    month: '2-digit',
    day: '2-digit'
  })
}

const getStatusColor = (status) => {
  const colors = {
    '草稿': 'grey',
    '已发布': 'success',
    '待审核': 'warning'
  }
  return colors[status] || 'grey'
}

const viewArticle = (id) => {
  router.push(`/articles/${id}`)
}

const editArticle = (id) => {
  router.push(`/articles/${id}/edit`)
}

const deleteArticle = (article) => {
  deleteTarget.value = article
  deleteDialog.value = true
}

const confirmDelete = async () => {
  // TODO: 调用API删除文章
  console.log('删除文章:', deleteTarget.value.id)
  deleteDialog.value = false
  deleteTarget.value = null
  // 重新加载列表
  await loadArticles()
}

const loadArticles = async () => {
  loading.value = true
  // TODO: 从API获取文章列表
  setTimeout(() => {
    articles.value = [
      {
        id: 1,
        title: '测试文章1',
        category: '技术',
        status: '已发布',
        created_at: '2025-01-15'
      },
      {
        id: 2,
        title: '测试文章2',
        category: '生活',
        status: '草稿',
        created_at: '2025-01-14'
      }
    ]
    loading.value = false
  }, 500)
}

onMounted(() => {
  loadArticles()
})
</script>
