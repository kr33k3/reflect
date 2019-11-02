import { Component } from '@angular/core';

import { Plugins } from '@capacitor/core';
const { SplashScreen, StatusBar } = Plugins;

import { Platform } from '@ionic/angular';

@Component({
  selector: 'app-root',
  templateUrl: 'app.component.html',
  styleUrls: ['app.component.scss']
})
export class AppComponent {
  constructor() {
    this.initializeApp();
  }

  initializeApp() {
    SplashScreen.hide().catch((err) => {
      console.warn(err);
      });
      StatusBar.hide().catch((err) => {
      console.warn(err);
      });
  }
}
