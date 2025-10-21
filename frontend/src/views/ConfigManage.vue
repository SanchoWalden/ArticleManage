<template>
  <div>
    <h1 class="text-h4 mb-6">配置管理</h1>

    <v-tabs v-model="tab">
      <v-tab value="profiles">写作配置 (Profiles)</v-tab>
      <v-tab value="briefs">需求文档 (Briefs)</v-tab>
    </v-tabs>

    <v-window v-model="tab" class="mt-4">
      <!-- Profiles 配置 -->
      <v-window-item value="profiles">
        <v-card>
          <v-card-title>
            <v-row>
              <v-col>写作风格配置</v-col>
              <v-col class="text-right">
                <v-btn color="primary" @click="openProfileDialog()">
                  <v-icon left>mdi-plus</v-icon>
                  新建配置
                </v-btn>
              </v-col>
            </v-row>
          </v-card-title>

          <v-card-text>
            <v-list>
              <v-list-item
                v-for="profile in profiles"
                :key="profile.id"
              >
                <template v-slot:prepend>
                  <v-icon>mdi-file-document</v-icon>
                </template>

                <v-list-item-title>{{ profile.name }}</v-list-item-title>
                <v-list-item-subtitle>{{ profile.description }}</v-list-item-subtitle>

                <template v-slot:append>
                  <v-btn icon size="small" @click="editProfile(profile)">
                    <v-icon>mdi-pencil</v-icon>
                  </v-btn>
                  <v-btn icon size="small" color="error" @click="deleteProfile(profile)">
                    <v-icon>mdi-delete</v-icon>
                  </v-btn>
                </template>
              </v-list-item>
            </v-list>
          </v-card-text>
        </v-card>
      </v-window-item>

      <!-- Briefs 需求文档 -->
      <v-window-item value="briefs">
        <v-card>
          <v-card-title>
            <v-row>
              <v-col>需求文档</v-col>
              <v-col class="text-right">
                <v-btn color="primary" @click="openBriefDialog()">
                  <v-icon left>mdi-plus</v-icon>
                  新建需求
                </v-btn>
              </v-col>
            </v-row>
          </v-card-title>

          <v-card-text>
            <v-list>
              <v-list-item
                v-for="brief in briefs"
                :key="brief.id"
              >
                <template v-slot:prepend>
                  <v-icon>mdi-text-box</v-icon>
                </template>

                <v-list-item-title>{{ brief.title }}</v-list-item-title>
                <v-list-item-subtitle>{{ formatDate(brief.created_at) }}</v-list-item-subtitle>

                <template v-slot:append>
                  <v-btn icon size="small" @click="editBrief(brief)">
                    <v-icon>mdi-pencil</v-icon>
                  </v-btn>
                  <v-btn icon size="small" color="error" @click="deleteBrief(brief)">
                    <v-icon>mdi-delete</v-icon>
                  </v-btn>
                </template>
              </v-list-item>
            </v-list>
          </v-card-text>
        </v-card>
      </v-window-item>
    </v-window>

    <!-- Profile 编辑对话框 -->
    <v-dialog v-model="profileDialog" max-width="800">
      <v-card>
        <v-card-title>{{ profileForm.id ? '编辑配置' : '新建配置' }}</v-card-title>
        <v-card-text>
          <v-text-field
            v-model="profileForm.name"
            label="配置名称"
            variant="outlined"
          ></v-text-field>

          <v-textarea
            v-model="profileForm.description"
            label="描述"
            variant="outlined"
            rows="2"
          ></v-textarea>

          <v-textarea
            v-model="profileForm.content"
            label="配置内容 (Markdown)"
            variant="outlined"
            rows="15"
          ></v-textarea>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn @click="profileDialog = false">取消</v-btn>
          <v-btn color="primary" @click="saveProfile">保存</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <!-- Brief 编辑对话框 -->
    <v-dialog v-model="briefDialog" max-width="800">
      <v-card>
        <v-card-title>{{ briefForm.id ? '编辑需求' : '新建需求' }}</v-card-title>
        <v-card-text>
          <v-text-field
            v-model="briefForm.title"
            label="需求标题"
            variant="outlined"
          ></v-text-field>

          <v-textarea
            v-model="briefForm.content"
            label="需求内容"
            variant="outlined"
            rows="15"
          ></v-textarea>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn @click="briefDialog = false">取消</v-btn>
          <v-btn color="primary" @click="saveBrief">保存</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const tab = ref('profiles')

const profiles = ref([])
const briefs = ref([])

const profileDialog = ref(false)
const briefDialog = ref(false)

const profileForm = ref({
  id: null,
  name: '',
  description: '',
  content: ''
})

const briefForm = ref({
  id: null,
  title: '',
  content: ''
})

const formatDate = (date) => {
  return new Date(date).toLocaleDateString('zh-CN')
}

const openProfileDialog = () => {
  profileForm.value = { id: null, name: '', description: '', content: '' }
  profileDialog.value = true
}

const editProfile = (profile) => {
  profileForm.value = { ...profile }
  profileDialog.value = true
}

const deleteProfile = async (profile) => {
  // TODO: 调用API删除
  console.log('删除Profile:', profile.id)
}

const saveProfile = async () => {
  // TODO: 调用API保存
  console.log('保存Profile:', profileForm.value)
  profileDialog.value = false
}

const openBriefDialog = () => {
  briefForm.value = { id: null, title: '', content: '' }
  briefDialog.value = true
}

const editBrief = (brief) => {
  briefForm.value = { ...brief }
  briefDialog.value = true
}

const deleteBrief = async (brief) => {
  // TODO: 调用API删除
  console.log('删除Brief:', brief.id)
}

const saveBrief = async () => {
  // TODO: 调用API保存
  console.log('保存Brief:', briefForm.value)
  briefDialog.value = false
}

onMounted(async () => {
  // TODO: 加载数据
  profiles.value = []
  briefs.value = []
})
</script>
