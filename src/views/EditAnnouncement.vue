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
  data: function() {
    return {
      pk: this.$router.history.current.params.key,
    };
  },
};
</script>
