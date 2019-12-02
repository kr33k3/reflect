import { Component, OnInit } from '@angular/core';
import { ModalController } from '@ionic/angular';

@Component({
  selector: 'app-new-tag',
  templateUrl: './new-tag.component.html',
  styleUrls: ['./new-tag.component.scss'],
})
export class NewTagComponent implements OnInit {
  newTag: String;

  constructor(private modalContrller: ModalController) { }

  ngOnInit() {}

  onSave() {
    this.modalContrller.dismiss(this.newTag)
  }

  onDismiss() {
    this.modalContrller.dismiss()
  }

}
