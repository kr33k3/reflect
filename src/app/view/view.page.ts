import { Component, OnInit } from '@angular/core';
import { MemoryService } from '../services/memory.service';
import { Memory } from '../models';
import { ModalController } from '@ionic/angular';
import { MemoryNewComponent } from '../memory/memory-new/memory-new.component';
import { MemoryViewComponent } from '../memory/memory-view/memory-view.component';

@Component({
  selector: 'app-view',
  templateUrl: './view.page.html',
  styleUrls: ['./view.page.scss'],
})
export class ViewPage implements OnInit {
  memories: Memory[]
  displaySearchBar = false;
  memoriesToDisplay: Memory[]

  constructor(private memoryService: MemoryService, private modalController: ModalController) {}

  ngOnInit() {
     this.refreshMemories();
  }

  openAdd() {
   this.newMemory();
  }

  async newMemory() {
    const modal = await this.modalController.create({
      component: MemoryNewComponent,
      cssClass: 'memory-input-modal'
    })

    modal.onDidDismiss().then((data) =>
    {
      if (data.data == null) {
        console.log('No Memory Returned');
        return;
      }
      this.memoryService.addMemories(data.data).then(() => this.refreshMemories())
    })
    return await modal.present();
  }

  refreshMemories() {
    this.memoryService.getMemories().then(data => {
      this.memories = data;
      if (this.memoriesToDisplay == null) {
        this.memoriesToDisplay = data;
      }
      console.log(data);
    })
  }

  openView(memory) {
    this.viewMemory(memory)
  }

  async viewMemory(memory) {
    const modal = await this.modalController.create({
      component: MemoryViewComponent,
      componentProps: {memory},
      cssClass: 'memory-input-modal'
    })

    modal.onDidDismiss().then((data) =>
    {
      if (data.data == null) {
        console.log('No Memory Returned')
        return
      }
      // TODO: Make update memories
      // this.memoryService.addMemories(data.data).then(() => this.refreshMemories())
    })
    return await modal.present();
  }

  sortMemories(event) {
    console.log(event)
  }

  filterMemories(event) {
    console.log(event)
    var filteredMemories = this.memories.filter( x=> {
      var index = x.Tags.findIndex( y => { return y == event})
      return index != -1
    })
    console.log(filteredMemories)
    this.memoriesToDisplay = event == '' ? this.memories : filteredMemories;
  }

  toggleSearchBar() {
    this.displaySearchBar = !this.displaySearchBar;
  }

}
