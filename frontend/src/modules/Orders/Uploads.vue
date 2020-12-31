<template>
  <b-container fluid>
    <form
      action=""
      method="POST"
      enctype="multipart/form-data"
      @submit.prevent="submit"
    >
      <b-row class="full-height">
        <!-- column one  -->
        <div class="col-lg-2 mt-5">
          <b-row class="mx-2">
            <div class="list group">
              <div class="item-title ">
                <h6>
                  <span class="badge badge-pill badge-primary">1</span> Order
                  details
                </h6>
                <p class=" item-description text-muted  ml-4">
                  Fill in your order requirements.
                </p>
              </div>
            </div>
          </b-row>

          <b-row class="mx-2">
            <div class="list group">
              <div class="item-title">
                <h6>
                  <span class="badge badge-pill badge-primary">2</span>
                  Instructions
                </h6>
                <p class="item-description text-muted ml-4">
                  Leave instructions for your writer
                </p>
              </div>
            </div>
          </b-row>

          <b-row class="mx-2">
            <div class="list group">
              <div class=" item-title text-left">
                <h6>
                  <span class="badge badge-pill badge-primary">3</span> Upload
                  Files
                </h6>
                <p class="item-description text-muted mx-4">
                  Uploads files for assignments and materials
                </p>
              </div>
            </div>
          </b-row>

          <hr style=" background-color: #ffff;" class="" />

          <button
            class="btn btn-primary text-left mb-5 col-12"
            @click.prevent="Mydelete"
          >
            <i class="far fa-trash-alt"></i> Discard draft
          </button>

          <div style="position: absolute; bottom: 0px;">
            <p class="item-description2 text-muted">
              You can return to the previous step and change any details if
              necessary.
            </p>

            <!-- <router-link to ="/orderdetails" class="link"><button class="btn  btn-primary text-center col-md-12 "> <i class="fas fa-arrow-left"></i>   Previous  </button></router-link> -->
            <button
              class="btn  btn-primary text-center col-md-12 "
              @click="$router.go(-1)"
            >
              <i class="fas fa-arrow-left"></i> Previous
            </button>
          </div>
        </div>
        <!-- column one  -->

        <!-- column two  -->
        <div class="col-lg-8 full-height">
          <div class=" ">
            <h1 class="text-left">
              <strong>
                Order {{ $route.params.id }}
                <span style="color: #e47c2a"> (Draft) </span>
              </strong>
            </h1>
            <div class="ant-card text-left px-3 py-4">
              <!-- display files uploaded  -->
              <div class="mt-4" v-if="this.filelist.length" v-cloak>
                <p class="" v-for="(file, index) in filelist" :key="index">
                  <i class="fas fa-paperclip"></i> {{ file.name }}
                  <a
                    type="button"
                    class="green-text"
                    title="Remove file"
                    @click.prevent="remove(filelist.indexOf(file))"
                    ><i class="fas fa-trash"></i
                  ></a>
                </p>
              </div>
              <!-- display files uploaded  -->

              <!-- display loading   -->
              <div class="filezone" v-if="loading">
                <div v-if="upload - done">
                  <p class="text-center mt-3">Uploading ....</p>

                  <div class="text-center ">
                    <div
                      class="spinner-border text-primary"
                      style="width: 10rem; height: 10rem;"
                      role="status"
                    >
                      <span class="sr-only">Loading...</span>
                    </div>
                  </div>
                </div>

                <!-- upload suceessful  -->
                <div v-else class="mt-5 text-center">
                  <i class="fas fa-check fa-5x " style="color:green;"></i>
                  Upload Successful
                </div>
                <!-- upload suceessful  -->
              </div>
              <!-- display loading   -->

              <div
                v-else
                class=" filezone my-3 mx-3 text-center "
                @dragover="dragover"
                @dragleave="dragover"
                @drop="drop"
              >
                <!-- display files uploaded  -->
                <div class="row" v-if="this.filelist.length" v-cloak>
                  <!-- <p class="mt-5 ml-5" v-for="(file, index) in filelist" :key="index" >
                                 <i class="fas fa-paperclip"></i>   {{file.name}}      <a type="button"  class="green-text" title="Remove file" @click.prevent="remove(filelist.indexOf(file))"><i class="fas fa-trash"></i></a>
                                 </p> -->

                  <div v-for="(file, index) in filelist" :key="index">
                    <v-chip
                      class="mt-3 mx-5"
                      close
                      color="green"
                      outlined
                      @click:close="filelist.splice(index, 1)"
                    >
                      {{ file.name }}
                    </v-chip>
                  </div>
                </div>
                <!-- display files uploaded  -->

                <div class="in-content">
                  <input
                    type="file"
                    multiple
                    id="id_files"
                    class="inputfile"
                    @change="inputFile"
                  />
                  <label for="id_files">
                    To Upload Files, Click Here or Drag and Drop
                  </label>
                </div>
              </div>

              <div class="text-center">
                <button type="submit" class="btn btn-primary ">Upload</button>
              </div>
            </div>
          </div>
        </div>

        <!-- column two  -->

        <!-- column three  -->
        <div class="col-lg-2 mt-5">
          <div class="ant-card mt-2 mb-5">
            Order draft
          </div>

          <div style="position: absolute; bottom: 0px;">
            <div class="ant-card mr-2 mt-5 mb-3 text-left px-3 py-4">
              <h5 class="item-title">Summary:</h5>
              <div class="item-description2">
                <p>
                  Quantity: <span class="text-muted "> 2 page / 550 words</span>
                </p>
                <p>
                  Deadline:<span class="text-muted"> 08/11/20, 06:04 PM </span>
                </p>
                <p>Level: <span class="text-muted"> College </span></p>
              </div>
            </div>

            <button
              class="btn btn-primary text-center col-md-12"
              @click.prevent="next"
            >
              Next Step <i class="fas fa-arrow-right"></i>
            </button>
          </div>
        </div>
        <!-- column three  -->
      </b-row>
    </form>
  </b-container>
</template>

<script>
import axios from "axios";
import router from "@/router";
export default {
  name: "Uploads",

  data() {
    return {
      message: "This is a form Component",
      filelist: [],
      id: "123",
      loading: false,
      upload_done: false
    };
  },

  mounted() {
    axios
      .get(`http://127.0.0.1:8000/api/uploads/${this.$route.params.id}/`)
      .then(res => {
        console.log(res.data);
        this.filelist.push();
      });
  },
  methods: {
    dragover() {
      event.preventDefault();
      // Add some visual fluff to show the user can drop its files
      if (!event.currentTarget.classList.contains("bg-green-300")) {
        // event.currentTarget.classList.remove('bg-gray-100');
        event.currentTarget.classList.add("bg-green-300");
      }
    },

    drop(event) {
      event.preventDefault();

      var files = event.dataTransfer.files;
      // this.filelist.(files)
      [...files].forEach(this.updateFileList);

      // console.log(files);

      event.currentTarget.classList.remove("bg-green-300");
    },

    inputFile(e) {
      console.log(e.target.files);
      var fileinputs = e.target.files;

      // this.filelist.(files)
      [...fileinputs].forEach(this.updateFileList);
    },

    dragleave() {},
    remove(i) {
      this.filelist.splice(i, 1);
    },
    updateFileList(file) {
      console.log(file, "this is file");
      this.filelist.push(file);
      let formData = new FormData();
      formData.append("file", file);
      console.log(formData, "this is form data");

      console.log(this.filelist[0], "this is file list");
      var filezone = document.getElementsByClassName("filezone");
      var incontent = document.getElementsByClassName("in-content");
      if (this.filelist.length !== 0) {
        for (let i = 0; i < filezone.length; i++) {
          filezone[i].style.height = "250px";
          incontent[i].style["margin-top"] = "10px";
        }
      } else {
        for (let i = 0; i < filezone.length; i++) {
          filezone[i].style.height = "450px";
        }
      }

      // let url = 'YOUR URL HERE'
    },
    submit() {
      this.loading = !this.loading;
      // this.upload_done = !this.upload_done

      let formData = new FormData();

      for (let i = 0; i < this.filelist.length; i++) {
        console.log(i, "this is i");
        formData.append("file-" + i, this.filelist[i]);
      }

      console.log(formData, "this is the formdata");
    },
    Mydelete() {
      axios
        .delete(
          `http://127.0.0.1:8000/api/orderdetailsdraft/${this.$route.params.id}/`,
          {
            body: { delete: "delete" }
          }
        )
        .then(res => {
          console.log(res.data);
          // var qs = res.data.qs
          console.log(res.data);

          if (res.data.deleted) {
            router.push("/orderdetails/");
          }
        })
        .catch(e => {
          console.log(e);
        });
    },
    next() {
      router.push("/dashboard/");
    }
  }
};
</script>

<style scoped>
.full-height {
  height: 600px;
}

.item-title {
  font-size: 12px !important;
  text-align: left !important;
}

.item-description {
  font-size: 11px !important;
  text-align: left !important;
}

.item-description2 {
  font-size: 13px !important;
  text-align: left !important;
}
.item-description2 .text-muted {
  font-size: 12px;
  align-content: center;
}

.filezone {
  border: rgba(12, 236, 236, 0.534) 5px dashed;
  font-size: 18px;
  align-content: center;
  height: 450px;
}

.filezone:hover {
  border: rgba(20, 236, 12, 0.534) 5px dashed;
}
.in-content {
  margin-top: 100px;
}

.bg-green-300 {
  background: #7ccee7;
}

.inputfile {
  width: 0.1px;
  height: 0.1px;
  opacity: 0;
  overflow: hidden;
  position: absolute;
  z-index: -1;
}
.inputfile + label {
  font-size: 1.25em;
  font-weight: 700;
  color: white;
  background-color: black;
  display: inline-block;
  cursor: pointer; /* "hand" cursor */
}

.inputfile:focus + label,
.inputfile + label:hover {
  background-color: red;
}
</style>
