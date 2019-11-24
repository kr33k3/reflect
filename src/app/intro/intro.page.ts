import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-intro',
  templateUrl: './intro.page.html',
  styleUrls: ['./intro.page.scss'],
})
export class IntroPage implements OnInit {

  constructor() { }

  ngOnInit() {
    var ionSlides = document.querySelector('ion-slides')
    //ionSlides.lockSwipes(true)
    ionSlides.slideNext()
    console.log('started I think')
  }

}
