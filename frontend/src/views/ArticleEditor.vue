<template>
  <div>
    <v-btn class="mb-4" @click="$router.back()">
      <v-icon left>mdi-arrow-left</v-icon>
      返回
    </v-btn>

    <v-card>
      <v-card-title>
        {{ isEdit ? '编辑文章' : '创建文章' }}
      </v-card-title>
      <v-card-text>
        <v-form ref="formRef" v-model="valid">
          <v-text-field
            v-model="form.title"
            label="文章标题"
            :rules="[rules.required]"
            variant="outlined"
          ></v-text-field>

          <v-select
            v-model="form.profile_id"
            label="选择写作配置"
            :items="profiles"
            item-title="name"
            item-value="id"
            variant="outlined"
          ></v-select>

          <v-select
            v-model="form.ai_model_id"
            label="选择AI模型"
            :items="aiModels"
            item-title="name"
            item-value="id"
            variant="outlined"
          ></v-select>

          <v-textarea
            v-model="form.brief"
            label="需求描述"
            :rules="[rules.required]"
            variant="outlined"
            rows="5"
          ></v-textarea>

          <v-btn
            color="primary"
            :loading="generating"
            @click="generateArticle"
            block
            class="mb-4"
          >
            <v-icon left>mdi-brain</v-icon>
            生成文章
          </v-btn>

          <v-textarea
            v-model="form.content"
            label="文章内容"
            variant="outlined"
            rows="20"
          ></v-textarea>
        </v-form>
      </v-card-text>

      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn @click="$router.back()">取消</v-btn>
        <v-btn color="primary" :loading="saving" @click="saveArticle">保存</v-btn>
      </v-card-actions>
    </v-card>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'

const route = useRoute()
const router = useRouter()

const formRef = ref(null)
const valid = ref(false)
const generating = ref(false)
const saving = ref(false)

const isEdit = computed(() => !!route.params.id)

const form = ref({
  title: '',
  profile_id: null,
  ai_model_id: null,
  brief: '',
  content: ''
})

const profiles = ref([])
const aiModels = ref([])

const rules = {
  required: value => !!value || '此字段必填'
}

const generateArticle = async () => {
  generating.value = true
  // TODO: 调用AI生成文章
  setTimeout(() => {
    form.value.content = '这是AI生成的文章内容...'
    generating.value = false
  }, 2000)
}

const saveArticle = async () => {
  if (!valid.value) return

  saving.value = true
  // TODO: 保存文章到后端
  setTimeout(() => {
    saving.value = false
    router.push('/articles')
  }, 1000)
}

onMounted(async () => {
  // TODO: 加载配置和模型列表
  profiles.value = [
    { id: 1, name: '科技测评-专业向' },
    { id: 2, name: '生产力工具-轻松向' }
  ]

  aiModels.value = [
    { id: 1, name: 'GPT-4' },
    { id: 2, name: 'Claude-3' }
  ]

  if (isEdit.value) {
    // TODO: 加载文章数据
  }
})
</script>
