<template>
  <div>
    <v-btn class="mb-4" @click="$router.back()">
      <v-icon left>mdi-arrow-left</v-icon>
      返回
    </v-btn>

    <v-card v-if="article">
      <v-card-title class="text-h4">{{ article.title }}</v-card-title>
      <v-card-subtitle>
        {{ formatDate(article.created_at) }} | {{ article.category }}
      </v-card-subtitle>
      <v-divider></v-divider>
      <v-card-text>
        <div v-html="article.content"></div>
      </v-card-text>
    </v-card>

    <v-card v-else>
      <v-card-text class="text-center pa-12">
        <v-progress-circular indeterminate></v-progress-circular>
      </v-card-text>
    </v-card>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const article = ref(null)

const formatDate = (date) => {
  return new Date(date).toLocaleDateString('zh-CN')
}

onMounted(async () => {
  // TODO: 从API获取文章详情
  setTimeout(() => {
    article.value = {
      id: route.params.id,
      title: '文章标题',
      category: '技术',
      created_at: '2025-01-15',
      content: '<p>文章内容...</p>'
    }
  }, 500)
})
</script>
