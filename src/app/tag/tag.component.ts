import { Component, OnInit, Input } from '@angular/core';
import { ModalController } from '@ionic/angular';
import { MemoryNewComponent } from '../memory/memory-new/memory-new.component';

@Component({
  selector: 'app-tag',
  templateUrl: './tag.component.html',
  styleUrls: ['./tag.component.scss'],
})
export class TagComponent implements OnInit {
  @Input() tags= ['Primary', 'Secondary', 'Tertiary'];
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
      component: MemoryNewComponent,
      cssClass: 'tag-input-modal'
    })

    return await modal.present();

  }

}
