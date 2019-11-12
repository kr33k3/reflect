import { Component, OnInit } from '@angular/core';
import { ModalController } from '@ionic/angular';

import { Memory } from '../../models';

@Component({
  selector: 'app-memory-new',
  templateUrl: './memory-new.component.html',
  styleUrls: ['./memory-new.component.scss'],
})
export class MemoryNewComponent implements OnInit {
  memory: Memory
  constructor(private modalController: ModalController) { 
    this.memory = {
      Title: 'Memory New',
      ContentList: [{Title: '', Body:'', Attachments: [], Tags: []}],
      DateCreated: new Date(),
      Type: ''
    }
  }

  ngOnInit() {}

  onSave() {
    console.log(this.memory)
    this.modalController.dismiss(this.memory)
  }

  onDismiss() {
    this.modalController.dismiss()
  }

}
