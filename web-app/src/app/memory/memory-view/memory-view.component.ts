import { Component, OnInit, Input } from '@angular/core';
import { ModalController } from '@ionic/angular';

@Component({
  selector: 'app-memory-view',
  templateUrl: './memory-view.component.html',
  styleUrls: ['./memory-view.component.scss'],
})
export class MemoryViewComponent implements OnInit {
  @Input() memory
  constructor(private modalController: ModalController) { }

  ngOnInit() {}
  
  onSave() {
    console.log(this.memory)
    this.modalController.dismiss(this.memory)
  }

  onDismiss() {
    this.modalController.dismiss()
  }
}
