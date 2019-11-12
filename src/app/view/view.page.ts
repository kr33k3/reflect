import { Component, OnInit } from '@angular/core';
import { MemoryService } from '../services/memory.service';
import { Memory } from '../models';
import { ModalController } from '@ionic/angular';
import { MemoryNewComponent } from '../memory/memory-new/memory-new.component';

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
     this.refreshMemories();
  }

  openAdd() {
   this.presentModal();
  }

  async presentModal() {
    const modal = await this.modalController.create({
      component: MemoryNewComponent
    })

    modal.onDidDismiss().then((data) =>
    {
      if (data.data == null) {
        console.log('No Memory Returned')
        return
      }
      this.memoryService.addMemories(data.data).then(() => this.refreshMemories())
    })
    return await modal.present();
  }

  refreshMemories() {
    this.memoryService.getMemories().then(data => {
      this.memories = data;
      console.log(data);
    })
  }

}
