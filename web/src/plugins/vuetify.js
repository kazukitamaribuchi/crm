import Vue from 'vue'
import Vuetify, {
    VApp,
    VContainer,
    VCard,
    VCardTitle,
    VCardText,
    VCardActions,
    VRow,
    VCol,
    VForm,
    VTextField,
    VList,
    VListItem,
    VListItemTitle,
    VListItemIcon,
    VIcon,
    VSpacer,
    VBtn,
} from 'vuetify/lib'



Vue.use(Vuetify, {
    components: {
        VApp,
        VContainer,
        VCard,
        VCardTitle,
        VCardText,
        VCardActions,
        VRow,
        VCol,
        VForm,
        VTextField,
        VList,
        VListItem,
        VListItemTitle,
        VListItemIcon,
        VIcon,
        VSpacer,
        VBtn,
    }
})

export default new Vuetify({
})
