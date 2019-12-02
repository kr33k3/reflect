import { Component, OnInit, Input } from '@angular/core';
import { ModalController } from '@ionic/angular';
import { NewTagComponent } from './new-tag/new-tag.component';

@Component({
  selector: 'app-tag',
  templateUrl: './tag.component.html',
  styleUrls: ['./tag.component.scss'],
})
export class TagComponent implements OnInit {
  @Input() tags: string[];
  constructor(private modalController: ModalController) { }

  ngOnInit() {
    console.log('Tag Component initialization ')
    console.log(this.tags)
  }

  logStuff() {
    console.log('Logged chip')
  }

  async addNewTag() {
    const modal = await this.modalController.create({
      component: NewTagComponent,
      cssClass: 'tag-input-modal'
    })

    modal.onDidDismiss().then(tag => {
      if(tag.data) {
        console.log(tag.data)
        this.tags.push(tag.data)
        return
      }
      console.log('No Data returned')
    })

    return await modal.present();
  }

  removeTag(index: number) {
    console.log(index)
    console.log(this.tags)
    this.tags.splice(index, 1)
    console.log(this.tags)
  }

}
