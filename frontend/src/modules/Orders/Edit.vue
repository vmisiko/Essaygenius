<template>

  <div class="hello">
    <div  v-cloak @drop.prevent="addFile" @dragover.prevent>
      <h2>Files to Upload (Drag them over)</h2>
      <ul>
        <li v-for="(file, index) in files" :key="index" >
          {{ file.name }} ({{ file.size }} kb) <button @click="removeFile(file)" title="Remove">X</button>
        </li>
      </ul>
      <button :disabled="uploadDisabled" @click="upload">Upload</button>
    </div>

   </div>
</template>

<script>
export default {
  name: 'Edit',
  data () {
    return {
      files:[]
    }
  },

  computed: {
    uploadDisabled() {
      return this.files.length === 0;
    }
  },
  
  methods:{
    addFile(e) {
      let droppedFiles = e.dataTransfer.files;
      if(!droppedFiles) return;
      console.log(droppedFiles);
      // this tip, convert FileList to array, credit: https://www.smashingmagazine.com/2018/01/drag-drop-file-uploader-vanilla-js/
      ([...droppedFiles]).forEach(f => {
        this.files.push(f);
      });
    },
    removeFile(file){
      this.files = this.files.filter(f => {
        return f != file;
      });      
    },


    upload() {
      
      let formData = new FormData();
      this.files.forEach((f,x) => {
        formData.append('file'+(x+1), f);
      });
      
      fetch('https://httpbin.org/post', {
        method:'POST',
        body: formData
      })
      .then(res => res.json())
      .then(res => {
         console.log('done uploading', res);
      })
      .catch(e => {
        console.error(JSON.stringify(e.message));
      });
      
    }
  }





}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
