<template>
  <v-row justify="center" align="center">
    <v-col cols="12" sm="8" md="6">
      <v-card tile flat color="transparent">

        <v-alert
          v-model="Warning"
          border="left"
          close-text="Close Alert"
          color="#2e2e2e"
          dark tile class="text-body-2"
          dismissible
        >
        <span class="text-h6 font-weight-normal">Warning: </span>This feature is currently in beta and is undergoing extensive testing to ensure optimal performance. As such, it may not function as intended and may contain bugs or other issues that could potentially impact the app. We strongly recommend using it only for testing purposes.
        </v-alert>

        <v-card tile flat class="pa-4" v-if="backendURL === 'http://127.0.0.1:8000'">
          <span class="my-1 text-justify">
            <v-icon class="mb-1">mdi-information-variant</v-icon> Server URL is set to localhost. A server must be running on your device to use this feature.
          </span>
        </v-card>

        <v-card color="transparent" tile>
          <v-card-title class="text-center justify-center py-6">
            <h1 class="font-weight-light text-h5 basil--text">
              Developer Preview
            </h1>
          </v-card-title>

          <v-tabs
            v-model="tab"
            background-color="transparent"
            color="basil"
            grow
          >
            <v-tab>
              Create
            </v-tab>

            <v-tab>
              Decode
            </v-tab>
          </v-tabs>

          <v-tabs-items v-model="tab">
            <v-tab-item>
              <v-card flat>
                
              <v-container fluid class="mt-4 pb-4">
                <span class="my-1 text-justify">
                  <v-icon class="mb-1">mdi-information-variant</v-icon> Enter the text you would like to encode into Pixeletted image. (Max 500 characters)
                </span>

                <v-textarea
                  name="user-data" rows="10" class="pt-5"
                  filled clear-icon="mdi-close-circle"
                  label="Your text" counter="500"
                  auto-grow clearable v-model="userData"
                ></v-textarea>

                <v-btn block tile outlined color="indigo" class="mt-2" @click="encode()">
                  <v-icon left>mdi-source-commit-start-next-local</v-icon>
                  Generate
                </v-btn>

              </v-container>

              </v-card>
            </v-tab-item>

            <v-tab-item>
              <v-card flat>

                <v-container fluid class="mt-4 pb-4">

                  <span class="my-1 text-justify">
                    <v-icon class="mb-1">mdi-information-variant</v-icon> Please select the Pixeletted image file that you would like to decode.
                  </span>

                  <form method="post">

                    <v-file-input
                      label="File input"
                      filled class="pt-6" name="pixelpic"
                      prepend-icon="mdi-camera"
                    ></v-file-input>

                  </form>

                  <v-btn block tile outlined color="indigo" class="mt-2" @click="decode()">
                    <v-icon left>mdi-source-commit-start-next-local</v-icon>
                    Process
                  </v-btn>

              </v-container>

              </v-card>
            </v-tab-item>
          </v-tabs-items>
        </v-card>

        <v-alert
          border="left"
          color="#2e2e2e"
          dark tile class="my-4 mt-8"
        >
        Please keep in mind that the data you'll enter will not be formatted perfectly due to testing. Thank you for your understanding and helping us to make this feature the best it can be.
        </v-alert>

        <v-expansion-panels>
          <v-expansion-panel>
            <v-expansion-panel-header>
              Developer Options
            </v-expansion-panel-header>
            <v-expansion-panel-content>

              <span class="my-1 text-justify">
                <v-icon class="mb-1">mdi-information-variant</v-icon> Please enter the server URL you would like to use for this testing.
              </span>

              <v-text-field class="mt-4"
                label="Pixelette Server URL" v-model="backendURL" hint="Local servers are for testing purposes only."
              ></v-text-field>

            </v-expansion-panel-content>
          </v-expansion-panel>
        </v-expansion-panels>

        <v-card color="transparent" tile flat>
          <v-img
            max-width="80" class="mx-auto mt-8 mb-4"
            src="Sykaa-logo.png" contain
          ></v-img>
        </v-card>

        <v-card tile flat color="transparent" height="60">
        </v-card>

      </v-card>

      <v-dialog
          v-model="overlay"
          hide-overlay persistent
          transition="dialog-bottom-transition"
          max-width="290" color="transparent" class="transparent"
        >
          <v-card class="pb-2">
            <v-toolbar
              dark tile flat
            >
              <v-btn
                icon
                dark
                @click="closeDialog()"
              >
                <v-icon>mdi-close</v-icon>
              </v-btn>
              <v-toolbar-title>Pixellete</v-toolbar-title>
              <v-spacer></v-spacer>
                <v-btn
                  icon @click="download()"
                  dark v-if="!errorMessage"
                >
                  <v-icon>mdi-progress-download</v-icon>
                </v-btn>
            </v-toolbar>

            <v-card tile flat>
              <v-alert
                v-model="SuccessPixel"
                border="left" v-if="!errorMessage"
                close-text="Close Alert"
                color="#2e2e2e"
                dark tile class="mb-n2"
              >
              <span class="text-h6 font-weight-normal">Success: </span> Your image has been successfully encoded. Please click the download button to save it to your device.
              </v-alert>

              <v-alert
                border="left" v-if="errorMessage"
                close-text="Close Alert"
                color="#2e2e2e"
                dark tile class="mb-n2"
              >
              <span class="text-h6 font-weight-normal">Failed: </span> {{ errorMessage }}
              </v-alert>

            </v-card>

          </v-card>
        </v-dialog>

        <v-dialog
          v-model="decodeOverlay"
          hide-overlay fullscreen
          transition="dialog-bottom-transition"
          max-width="290" color="transparent" class="transparent"
        >
          <v-card class="pb-2">
            <v-toolbar
              dark tile flat
            >
              <v-btn
                icon
                dark
                @click="decodeOverlay = false"
              >
                <v-icon>mdi-close</v-icon>
              </v-btn>
              <v-toolbar-title>Pixellete</v-toolbar-title>
              <v-spacer></v-spacer>
                <v-btn
                  icon @click="copyText()"
                  dark v-if="!errorMessage"
                >
                  <v-icon>mdi-content-copy</v-icon>
                </v-btn>
            </v-toolbar>

            <v-card tile flat>
              <v-alert
                border="left" v-if="!errorMessage"
                close-text="Close Alert"
                color="#2e2e2e"
                dark tile class="mb-n2"
              >
              <span class="text-h6 font-weight-normal">Success: </span> Your image has been successfully decoded. Please click the copy button to copy the contents.
              </v-alert>

              <v-alert
                border="left" v-if="errorMessage"
                close-text="Close Alert"
                color="#2e2e2e"
                dark tile class="mb-n2"
              >
              <span class="text-h6 font-weight-normal">Failed: </span> {{ errorMessage }}
              </v-alert>

              <v-card-text>

                <v-textarea
                  rows="10" class="pt-5" v-if="!errorMessage"
                  filled clear-icon="mdi-close-circle"
                  label="Decoded text" readonly ref="dataText"
                  auto-grow clearable v-model="pixelText"
                ></v-textarea>

              </v-card-text>

            </v-card>

          </v-card>
        </v-dialog>

    </v-col>
  </v-row>
</template>

<script>
export default {
  name: 'CustomPage',
  data () {
    return {
      Warning: true,
      tab: null,
      userData: null,
      pixelData: "",
      backendURL: "http://127.0.0.1:8000",
      overlay: false,
      decodeOverlay: false,
      errorMessage: null,
      SuccessPixel: true,
      pixelLink: null,
      pixelText: null,
    }
  },

  methods: {
    closeDialog() {
      this.overlay = !this.overlay
      this.errorMessage = null
    },

    async encode() {
      this.overlay = true
      try {
        await this.$axios
          .post(this.backendURL + '/api/encode/', { 
            'text': this.userData,
          })
          .then((res) => {
            this.pixelData = res.data
            this.pixelLink = this.backendURL + res.data["link"]
          })
          .catch((err) => {
            this.errorMessage = err
          })
      } catch (error) {
        // this.$sentry.captureException(new Error(error))
      }
    },

    async decode() {
      this.decodeOverlay = true
      const headers = {
        'Content-Type': 'multipart/form-data',
      }
      
      const form = document.querySelector("form");
      var formData = new FormData(form);

      try {
        await this.$axios
          .post(this.backendURL + '/api/decode/', formData, { headers: headers })
          .then((res) => {
            this.pixelData = res.data
            this.pixelText = res.data["data"]
          })
          .catch((err) => {
            this.errorMessage = err
          })
      } catch (error) {
        // this.$sentry.captureException(new Error(error))
      }
    },

    download() {
      let url = this.pixelLink;
      fetch(url)
        .then((response) => response.blob())
        .then(blob => {
          let blobUrl = window.URL.createObjectURL(blob);
          let a = document.createElement('a');
          a.download = url.replace(/^.*[\\\/]/, '');
          a.href = blobUrl;
          document.body.appendChild(a);
          a.click();
          a.remove();
        });
      console.log('downloading', url);
    },

    copyText() {
      navigator.clipboard.writeText(this.pixelText);
    }
  }

}
</script>