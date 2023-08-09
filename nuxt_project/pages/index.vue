<template>
  <v-row justify="center" align="center">
    <v-col cols="12" sm="8" md="6">
      <v-card tile flat color="transparent">

        <v-img
          src="new-banner.png" max-height="700" contain
        ></v-img>

        <v-card-title class="headline font-weight-light">
          Why Pixelette
        </v-card-title>

        <v-card-text>
          <p>{{ Description }}</p>
        </v-card-text>

        <v-btn
          class="ml-4 mb-4"
          outlined tile
          color="indigo"
        >
        <v-icon left>mdi-play-circle-outline</v-icon>
          Visit Site
        </v-btn>

        <v-card-title class="headline font-weight-light mt-0">
          How it works
        </v-card-title>

        <v-card-text>
          <p>{{ Working }}</p>
        </v-card-text>

        <v-btn
          class="ml-4 mb-4"
          outlined tile
          color="indigo"
        >
        <v-icon left>mdi-file-document</v-icon>
          Documentations
        </v-btn>

        <v-card color="transparent" tile flat>
          <v-img
            max-width="80" class="mx-auto mt-4" contain
            src="Sykaa-logo.png"
          ></v-img>
        </v-card>

        <v-card tile flat color="transparent" height="60">
        </v-card>

          <br>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
export default {
  name: 'IndexPage',
  data () {
      return {
        Description: 'Pixelette enables users to encode any text into pixels of an image. This app is designed to provide a highly secure method of data transfer by transforming text into an image format that is impossible to decode without the proper tools.',
        Working: 'Pixelette works by converting the text input into binary code, which is then used to generate pixel data for an image. The app allows users to select an image of their choice or use one of the pre-built images provided by the app as the canvas for the encoded message.',
      }
  },
}
</script>
