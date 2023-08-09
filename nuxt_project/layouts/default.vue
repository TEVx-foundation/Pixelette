<template>
  <v-app dark>
    <v-navigation-drawer
      v-model="drawer"
      :clipped="clipped"
      fixed
      app
    >

    <v-img src="pixelette-ico.png" class="mx-auto my-8" contain max-width="100"></v-img>

      <v-list shaped>
        <v-list-item
          v-for="(item, i) in items"
          :key="i"
          :to="item.to"
          router
          exact
        >
          <v-list-item-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>

      <template v-slot:append>
        <div class="pa-2 mx-auto">
          <v-card-text>Developer - Beta Release 2.1</v-card-text>
        </div>
      </template>

    </v-navigation-drawer>
    <v-app-bar
      :clipped-left="clipped"
      fixed color="#121212"
      app elevate-on-scroll
    >
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
      <v-toolbar-title>{{ title }}</v-toolbar-title>
      <v-spacer />

      <v-btn icon @click="GithubNotification = true">
        <v-icon>mdi-github</v-icon>
      </v-btn>

    </v-app-bar>
    <v-main>
      <v-container>
        <Nuxt />
      </v-container>

      

    </v-main>

    <v-snackbar tile
      v-model="GithubNotification"
    >
      Not Available for Testing Release

      <template v-slot:action="{ attrs }">
        <v-btn
          icon
          v-bind="attrs"
          @click="GithubNotification = false"
        >
          <v-icon>mdi-close</v-icon>
        </v-btn>
      </template>
    </v-snackbar>

    <v-bottom-navigation grow fixed>

        <v-btn value="create" to="/custom">
          <span>Create</span>

          <v-icon class="mb-1">mdi-pencil-outline</v-icon>
        </v-btn>

        <v-bottom-sheet
          v-model="donate"
          inset
        >
          <template v-slot:activator="{ on, attrs }">

            <v-btn value="favorites" v-bind="attrs" v-on="on">
              <span>Donate</span>

              <v-icon class="mb-1">mdi-heart</v-icon>
            </v-btn>

          </template>
          <v-card class="pb-2">
            <v-card-title class="text-h5">
              Donate
            </v-card-title>
            <v-card-text class="text-subtitle">We are constantly working to improve its features and functionality, so that you can have the best possible experience. However, we need your support to keep this app running and to continue providing you with new updates and improvements.</v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn class="mr-2"
                tile text
                @click="donate = false"
              >
                Later
              </v-btn>
              <v-btn
                color="green darken-1"
                tile outlined
                @click="donate = false"
              >
                Donate
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-bottom-sheet>

        <v-dialog
          v-model="developer"
          fullscreen
          hide-overlay
          transition="dialog-bottom-transition"
          max-width="290"
        >
          <template v-slot:activator="{ on, attrs }">

            <v-btn value="developer" v-bind="attrs" v-on="on">
              <span>Developer</span>
              <v-icon class="mb-1">mdi-dev-to</v-icon>
            </v-btn>

          </template>
          <v-card class="pb-2">
            <v-toolbar
              dark tile flat
            >
              <v-btn
                icon
                dark
                @click="developer = false"
              >
                <v-icon>mdi-close</v-icon>
              </v-btn>
              <v-toolbar-title>Developer</v-toolbar-title>
              <v-spacer></v-spacer>
                <v-btn
                  icon
                  dark
                >
                  <v-icon>mdi-launch</v-icon>
                </v-btn>
            </v-toolbar>

            <v-card tile flat class="mx-auto pb-4">
              
              <v-card class="mx-auto"
                max-width="374" tile flat
              >

              <v-card-title class="mt-4">
                <v-avatar size="60">
                  <img alt="tevx" src="TEVx.png">
                </v-avatar>
                <p class="ml-3 mt-5 text-h6 font-weight-light">
                  Team Vertex Foundation
                </p>
              </v-card-title>

              <v-card-text class="mx-auto">
                <div class="mb-4 mt-n2 text-center text-overline">
                  Sykaa Platforms Authored ©
                </div>
                <div>We are few, yet a passionate who enjoy creating solutions to help people around the world. We are working to build a foundation where developers all around the world can collaborate and work together. Our works empower everyone in this world to share ideas, offer support and make a difference.</div>
              </v-card-text>

              <v-card-title class="headline font-weight-light mt-0">
                Our Vision
              </v-card-title>
              <v-card-text>
                <p>Keeping our mission in mind, we will bring a transformation in the life of tech enthusiasts and take the idea of education to another level. Nothing here is somebody else’s problem. If you roll up your sleeves, sometimes you’re able to make an impact where you may not have thought you could.</p>
              </v-card-text>

              <v-card-title class="headline font-weight-light mt-0">
                Get in Touch
              </v-card-title>
              <v-card-text>
                <p>If you have any questions or feedback regarding the application or would like to contact the developer, please feel free to leave a message at mail. The developer would be happy to hear from you and will try to respond as soon as possible.
                Thank you for your support and for using our application.</p>
                <v-icon>mdi-gmail</v-icon> <a href="mailto:teamvertex@gmail.com" class="text-decoration-none mx-2">teamvertex@gmail.com</a>
              </v-card-text>
              </v-card>

              <v-card color="transparent" tile flat>
                <v-img
                  max-width="100" class="mx-auto mt-8 mb-4"
                  src="Sykaa-logo.png" contain
                ></v-img>
              </v-card>

            </v-card>

          </v-card>
        </v-dialog>

      </v-bottom-navigation>

  </v-app>
</template>

<script>
export default {
  name: 'DefaultLayout',
  data () {
    return {
      clipped: false,
      drawer: false,
      fixed: false,
      donate: false,
      developer: false,
      GithubNotification: false,
      items: [
        {
          icon: 'mdi-apps',
          title: 'Overview',
          to: '/'
        },
        {
          icon: 'mdi-chart-bubble',
          title: 'Developer Preview',
          to: '/custom'
        }
      ],
      right: true,
      title: 'Pixelette'
    }
  }
}
</script>
