<template>
  <div>
    <h1 class="text-h4 mb-6">工作台</h1>

    <v-row>
      <v-col cols="12" md="3">
        <v-card color="primary" dark>
          <v-card-text>
            <div class="text-h6">文章总数</div>
            <div class="text-h3">{{ stats.articleCount }}</div>
          </v-card-text>
        </v-card>
      </v-col>

      <v-col cols="12" md="3">
        <v-card color="success" dark>
          <v-card-text>
            <div class="text-h6">配置数量</div>
            <div class="text-h3">{{ stats.profileCount }}</div>
          </v-card-text>
        </v-card>
      </v-col>

      <v-col cols="12" md="3">
        <v-card color="warning" dark>
          <v-card-text>
            <div class="text-h6">AI模型</div>
            <div class="text-h3">{{ stats.aiModelCount }}</div>
          </v-card-text>
        </v-card>
      </v-col>

      <v-col cols="12" md="3">
        <v-card color="info" dark>
          <v-card-text>
            <div class="text-h6">需求文档</div>
            <div class="text-h3">{{ stats.briefCount }}</div>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>

    <v-row class="mt-6">
      <v-col cols="12" md="8">
        <v-card>
          <v-card-title>最近文章</v-card-title>
          <v-card-text>
            <v-list>
              <v-list-item
                v-for="article in recentArticles"
                :key="article.id"
                :to="`/articles/${article.id}`"
              >
                <v-list-item-title>{{ article.title }}</v-list-item-title>
                <v-list-item-subtitle>{{ formatDate(article.created_at) }}</v-list-item-subtitle>
              </v-list-item>
            </v-list>
          </v-card-text>
        </v-card>
      </v-col>

      <v-col cols="12" md="4">
        <v-card>
          <v-card-title>快速操作</v-card-title>
          <v-card-text>
            <v-btn
              color="primary"
              block
              class="mb-3"
              to="/articles/create"
            >
              <v-icon left>mdi-plus</v-icon>
              创建新文章
            </v-btn>
            <v-btn
              color="success"
              block
              class="mb-3"
              to="/configs"
            >
              <v-icon left>mdi-cog</v-icon>
              管理配置
            </v-btn>
            <v-btn
              color="info"
              block
              to="/ai-models"
            >
              <v-icon left>mdi-brain</v-icon>
              AI模型设置
            </v-btn>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const stats = ref({
  articleCount: 0,
  profileCount: 0,
  aiModelCount: 0,
  briefCount: 0
})

const recentArticles = ref([])

const formatDate = (date) => {
  return new Date(date).toLocaleDateString('zh-CN')
}

onMounted(async () => {
  // TODO: 从API获取统计数据
  stats.value = {
    articleCount: 12,
    profileCount: 5,
    aiModelCount: 3,
    briefCount: 8
  }

  recentArticles.value = []
})
</script>
