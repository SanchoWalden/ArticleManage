<template>
  <div>
    <v-row class="mb-4">
      <v-col cols="12" md="6">
        <h1 class="text-h4">AI模型配置</h1>
      </v-col>
      <v-col cols="12" md="6" class="text-right">
        <v-btn color="primary" @click="openDialog()">
          <v-icon left>mdi-plus</v-icon>
          添加模型
        </v-btn>
      </v-col>
    </v-row>

    <v-row>
      <v-col
        v-for="model in aiModels"
        :key="model.id"
        cols="12"
        md="6"
        lg="4"
      >
        <v-card>
          <v-card-title>
            <v-icon left :color="model.enabled ? 'success' : 'grey'">
              mdi-brain
            </v-icon>
            {{ model.name }}
          </v-card-title>

          <v-card-subtitle>
            {{ model.provider }} - {{ model.model_name }}
          </v-card-subtitle>

          <v-card-text>
            <v-list dense>
              <v-list-item>
                <v-list-item-title>Temperature</v-list-item-title>
                <v-list-item-subtitle>{{ model.temperature }}</v-list-item-subtitle>
              </v-list-item>
              <v-list-item>
                <v-list-item-title>Max Tokens</v-list-item-title>
                <v-list-item-subtitle>{{ model.max_tokens }}</v-list-item-subtitle>
              </v-list-item>
              <v-list-item>
                <v-list-item-title>优先级</v-list-item-title>
                <v-list-item-subtitle>{{ model.priority }}</v-list-item-subtitle>
              </v-list-item>
            </v-list>

            <v-chip
              :color="model.enabled ? 'success' : 'grey'"
              small
              class="mt-2"
            >
              {{ model.enabled ? '已启用' : '已禁用' }}
            </v-chip>
          </v-card-text>

          <v-card-actions>
            <v-btn size="small" @click="editModel(model)">编辑</v-btn>
            <v-btn size="small" @click="toggleModel(model)">
              {{ model.enabled ? '禁用' : '启用' }}
            </v-btn>
            <v-spacer></v-spacer>
            <v-btn size="small" color="error" @click="deleteModel(model)">删除</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>

    <!-- 模型配置对话框 -->
    <v-dialog v-model="dialog" max-width="600">
      <v-card>
        <v-card-title>{{ modelForm.id ? '编辑模型' : '添加模型' }}</v-card-title>
        <v-card-text>
          <v-text-field
            v-model="modelForm.name"
            label="显示名称"
            variant="outlined"
          ></v-text-field>

          <v-select
            v-model="modelForm.provider"
            label="服务商"
            :items="providers"
            variant="outlined"
          ></v-select>

          <v-text-field
            v-model="modelForm.model_name"
            label="模型名称"
            hint="例如: gpt-4, claude-3-opus"
            variant="outlined"
          ></v-text-field>

          <v-text-field
            v-model="modelForm.api_key"
            label="API Key"
            type="password"
            variant="outlined"
          ></v-text-field>

          <v-text-field
            v-model="modelForm.base_url"
            label="Base URL (可选)"
            hint="默认使用官方API地址"
            variant="outlined"
          ></v-text-field>

          <v-slider
            v-model="modelForm.temperature"
            label="Temperature"
            min="0"
            max="2"
            step="0.1"
            thumb-label
          ></v-slider>

          <v-text-field
            v-model.number="modelForm.max_tokens"
            label="Max Tokens"
            type="number"
            variant="outlined"
          ></v-text-field>

          <v-text-field
            v-model.number="modelForm.priority"
            label="优先级"
            type="number"
            hint="数字越大优先级越高"
            variant="outlined"
          ></v-text-field>

          <v-switch
            v-model="modelForm.enabled"
            label="启用此模型"
            color="primary"
          ></v-switch>
        </v-card-text>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn @click="dialog = false">取消</v-btn>
          <v-btn color="primary" @click="saveModel">保存</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const dialog = ref(false)
const aiModels = ref([])

const providers = [
  'OpenAI',
  'Anthropic',
  '文心一言',
  '通义千问',
  '智谱AI',
  '豆包',
  '其他'
]

const modelForm = ref({
  id: null,
  name: '',
  provider: '',
  model_name: '',
  api_key: '',
  base_url: '',
  temperature: 0.7,
  max_tokens: 4000,
  priority: 1,
  enabled: true
})

const openDialog = () => {
  modelForm.value = {
    id: null,
    name: '',
    provider: '',
    model_name: '',
    api_key: '',
    base_url: '',
    temperature: 0.7,
    max_tokens: 4000,
    priority: 1,
    enabled: true
  }
  dialog.value = true
}

const editModel = (model) => {
  modelForm.value = { ...model }
  dialog.value = true
}

const toggleModel = async (model) => {
  // TODO: 调用API切换状态
  model.enabled = !model.enabled
}

const deleteModel = async (model) => {
  // TODO: 调用API删除
  console.log('删除模型:', model.id)
}

const saveModel = async () => {
  // TODO: 调用API保存
  console.log('保存模型:', modelForm.value)
  dialog.value = false
}

onMounted(async () => {
  // TODO: 加载数据
  aiModels.value = [
    {
      id: 1,
      name: 'GPT-4',
      provider: 'OpenAI',
      model_name: 'gpt-4',
      temperature: 0.7,
      max_tokens: 4000,
      priority: 10,
      enabled: true
    }
  ]
})
</script>
