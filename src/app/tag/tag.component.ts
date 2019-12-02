import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-tag',
  templateUrl: './tag.component.html',
  styleUrls: ['./tag.component.scss'],
})
export class TagComponent implements OnInit {
  @Input() tags= ['Primary', 'Secondary', 'Tertiary'];
  constructor() { }

  ngOnInit() {
    console.log('Tag Component initialization ')
    console.log(this.tags)
  }

  logStuff() {
    console.log('Logged chip')
  }

}
