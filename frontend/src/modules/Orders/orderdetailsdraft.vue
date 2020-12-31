<template>
  <b-container fluid class="mt-5">
    <form
      action=""
      method="POST"
      enctype="multipart/form-data"
      @submit="submit"
    >
      <b-row>
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
        </div>
        <!-- column one  -->

        <!-- column two  -->
        <div class="col-lg-8">
          <div class=" ">
            <h1 class="text-left">
              <strong>
                Order {{ $route.params.id }}
                <span style="color: #e47c2a"> (Draft) </span>
              </strong>
            </h1>
            <div class="ant-card text-left px-3 py-4">
              <div class="row ">
                <div class="form-group col-lg-6 col-md-12">
                  <label for="id_type" class="form-control-label ">
                    Type
                  </label>

                  <input
                    v-model="form.type"
                    type="text"
                    name="type"
                    maxlength="255"
                    class="textinput textInput form-control"
                    id="id_topic"
                    required
                  />
                </div>

                <div class="form-group col-lg-6 col-md-12">
                  <label for="id_pages" class="col-form-label ">
                    Pages
                  </label>

                  <input
                    v-model="form.pages"
                    type="number"
                    name="pages"
                    value="0"
                    class="numberinput form-control form-control"
                    id="id_pages"
                    required
                  />
                </div>
              </div>

              <div class="row ">
                <div class="form-group col-lg-6 col-md-12">
                  <label for="id_service" class="col-form-label ">
                    Service
                  </label>

                  <select
                    v-model="form.service"
                    name="service"
                    class="browser-default custom-select mb-3"
                    required
                    id="id_service"
                  >
                    <option value="Writing" selected>Writing </option>

                    <option value="Rewriting">Rewriting</option>

                    <option value="Editing">Editing</option>

                    <option value="ProofReading"> Proof Reading</option>
                  </select>
                </div>

                <div class="form-group col-lg-6 col-md-12">
                  <label for="id_service" class="col-form-label ">
                    Level
                  </label>

                  <select
                    v-model="form.level"
                    name="category"
                    class="browser-default custom-select mb-3"
                    required
                    id="id_service"
                  >
                    <option value="School" selected> School </option>

                    <option value="COllege">College</option>

                    <option value="Univerisity">Univerisity</option>

                    <option value="Doctrate">Doctrate</option>
                  </select>
                </div>
              </div>

              <div class="row ">
                <div class="form-group col-lg-6 col-md-12">
                  <label for="id_deadline" class="form-control-label">
                    Deadline
                  </label>

                  <!-- <input type="number" name="amount" value="0.0" class="numberinput form-control form-control" id="id_deadline" required> -->
                  <datetime
                    id="id_deadline"
                    type="datetime"
                    v-model="form.deadline"
                    class="form-control"
                    required
                  ></datetime>
                </div>

                <div class="form-group col-lg-6 col-md-12"></div>
              </div>

              <div class="custom-control custom-checkbox form-group">
                <input
                  v-model="form.checkbox"
                  type="checkbox"
                  id="id_checkbox"
                  class="custom-control-input "
                  true-value="true"
                  false-value="False"
                />

                <label for="id_checkbox" class="custom-control-label">
                  I need the final answer earlier than the set Deadline
                </label>

                <!-- <textarea name="instructions" cols="40" rows="3" maxlength="5000" class="textarea form-control form-control" id="id_instructions"></textarea> -->
              </div>

              <b-row>
                <div class="form-group col-lg-6 col-md-12">
                  <label for="id_language" class="col-form-label ">
                    Language
                  </label>

                  <select
                    v-model="form.language"
                    name="language"
                    class="browser-default custom-select mb-3"
                    required
                    id="id_language"
                  >
                    <option value="English (UK)" selected>English (US) </option>

                    <option value="English (US)">English (UK)</option>
                  </select>
                </div>
              </b-row>
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
              type="submit"
              class="btn btn-primary text-center col-md-12 m"
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
import { Datetime } from "vue-datetime";
import router from "@/router";
import axios from "axios";

export default {
  name: "orderdetailsdraft",
  components: {
    datetime: Datetime
  },
  data() {
    return {
      message: "This is a form Component",
      form: {}
    };
  },
  mounted() {
    axios
      .get(
        `http://127.0.0.1:8000/api/orderdetailsdraft/${this.$route.params.id}/`
      )
      .then(res => {
        console.log(res.data);
        this.form = res.data;
      })
      .catch(e => {
        console.log(e);
      });
  },
  methods: {
    submit(e) {
      e.preventDefault();
      console.log(this.form);

      axios
        .put(
          `http://127.0.0.1:8000/api/orderdetailsdraft/${this.$route.params.id}/`,
          {
            body: this.form
          }
        )
        .then(res => {
          console.log(res.data);
          var qs = res.data.qs;
          // console.log(q)

          if (res.data.posted) {
            router.push("/instructions/" + qs);
          }
        })
        .catch(e => {
          console.log(e);
        });
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
    }
  }
};
</script>

<style scoped>
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
}
</style>
