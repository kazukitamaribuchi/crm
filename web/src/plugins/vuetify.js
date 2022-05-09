import Vue from 'vue'
import Vuetify, {
    VApp,
    VContainer,
    VCard,
    VCardTitle,
    VCardSubtitle,
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
    VSimpleTable,
    VDialog,
    VSelect,
    VListGroup,
    VListItemContent,
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
        VCardSubtitle,
        VSimpleTable,
        VDialog,
        VSelect,
        VListGroup,
        VListItemContent,
    }
})

export default new Vuetify({
})
