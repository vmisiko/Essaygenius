<template>
  <div class="mx-5">
    <v-list-item link dense>
      <div class="hovereffect">
        <v-row class="hovmargin">
          <v-col cols="5" class="mt-n4">
            <v-list-item two-line>
              <v-list-item-content>
                <v-list-item-title>{{ topic }}</v-list-item-title>
                <v-list-item-subtitle class="caption">
                  853679 | {{ pages }} pages | {{ type }} |
                  {{ language }}</v-list-item-subtitle
                >
              </v-list-item-content>
            </v-list-item>
          </v-col>

          <v-col class="d-flex justify-center">
            <v-chip class="pa-4 float-left" color="primary" label>
              Bidding
            </v-chip>
          </v-col>
          <v-col>
            <v-row>
              <v-col class="mt-n7">
                <v-list-item two-line>
                  <v-list-item-content>
                    <v-list-item-title class="float-right"
                      >~${{ amount }}</v-list-item-title
                    >
                    <v-list-item-subtitle class="caption"
                      >{{ time }}
                    </v-list-item-subtitle>
                  </v-list-item-content>
                </v-list-item>
              </v-col>
              <v-col class="mt-n4">
                <v-menu offset-y>
                  <template v-slot:activator="{ on, attrs }">
                    <v-btn color="" dark v-bind="attrs" v-on="on">
                      <i class="fas fa-ellipsis-v"></i>
                    </v-btn>
                  </template>
                  <v-btn> <i class="fas fa-trash"></i> Cancel Order </v-btn>
                </v-menu>
              </v-col>
            </v-row>
          </v-col>
        </v-row>
      </div>
    </v-list-item>
    <v-divider class="mt-n3"></v-divider>
  </div>
</template>

<script>
export default {
  name: "OpenedOrder",
  props: ["topic", "pages", "type", "language", "status", "amount", "time"]
};
</script>

<style scoped></style>
