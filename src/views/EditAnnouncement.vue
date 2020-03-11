<template>
  <div>
    <CreateAnnouncement :edit="true" :pk="pk" />
  </div>
</template>

<script>
import CreateAnnouncement from '@/views/CreateAnnouncement.vue';

export default {
  name: 'EditAnnouncement',
  components: {
    CreateAnnouncement,
  },
  props: {
    pk_key: String,
  },
  data: function() {
    return {
      pk: this.pk_key,
    };
  },
};
</script>
