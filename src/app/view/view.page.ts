import { Component, OnInit } from '@angular/core';
import { MemoryService } from '../services/memory.service';
import { Memory } from '../models';
import { ModalController } from '@ionic/angular';
import { MemoryInputComponent } from '../memory/memory-input/memory-input.component';

@Component({
  selector: 'app-view',
  templateUrl: './view.page.html',
  styleUrls: ['./view.page.scss'],
})
export class ViewPage implements OnInit {
  memories: Memory[]
  constructor(private memoryService: MemoryService, private modalController: ModalController) {

   }

  ngOnInit() {
     this.memoryService.getMemories().then(data => {
      this.memories = data
      console.log(data)
    })
  }

  openAdd() {
   this.presentModal();
  }

  async presentModal() {
    const modal = await this.modalController.create({
      component: MemoryInputComponent
    })

    modal.onDidDismiss().then((data) =>
    {
      console.log('Modal Dismissed')
    })
    return await modal.present();
  }

}
