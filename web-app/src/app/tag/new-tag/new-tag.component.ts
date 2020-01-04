import { Component, OnInit, HostListener } from '@angular/core';
import { ModalController } from '@ionic/angular';

@Component({
  selector: 'app-new-tag',
  templateUrl: './new-tag.component.html',
  styleUrls: ['./new-tag.component.scss'],
})
export class NewTagComponent implements OnInit {
  newTag: String;

  constructor(private modalContrller: ModalController) { }

  ngOnInit() {
  }

  onSave() {
    this.modalContrller.dismiss(this.newTag)
  }

  onDismiss() {
    this.modalContrller.dismiss()
  }
  @HostListener('window:keyup', ['$event'])
  keyEvent(event: KeyboardEvent) {
    if (event.code == 'Enter') {
      if (this.newTag) {
        this.onSave()
      } else {
        this.onDismiss()
      }
    }
  }
}
