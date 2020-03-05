<template>
  <div>
    <CreateAnnouncement :data_edit="data_pengumuman" edit="true" />
  </div>
</template>

<script>
import CreateAnnouncement from '@/views/CreateAnnouncement';
import announcementApi from '@/services/announcementServices';

export default {
  name: 'EditAnnouncement',
  component: CreateAnnouncement,
  data: function() {
    announcementApi.getAnnouncement().then((d) => {
      return d.data;
    });
  },
};
</script>
