import { Component, OnInit } from '@angular/core';
import { PickerController } from '@ionic/angular';

@Component({
  selector: 'app-search-bar',
  templateUrl: './search-bar.component.html',
  styleUrls: ['./search-bar.component.scss'],
})
export class SearchBarComponent implements OnInit {
  constructor(private pickerController: PickerController) { }
  sortItemOptions = [
      {
        name: 'Sort Item',
        options: [
        {
          text: 'Ranking',
          value: 'ranking'
        },
        {
          text: 'Date Created',
          value: 'dateCreated'
        }
      ]
    }
  ];

  sortOptions = [
    'Newest',
    'Oldest',
    'Most Recent',
    'Less Recent'
  ]

  ngOnInit() {
  }


  logChange(event) {
    console.log(event)
    console.log(event.target.value)
  }

  async openFilterPicker() {
    const picker = await this.pickerController.create({
      columns: this.sortItemOptions,
      buttons: [
        {
          text: 'Cancel',
          role: 'cancel'
        },
        {
          text: 'Confirm',
          handler: (value) => {
            console.log(value);
          }
        }
      ]
    });
    await picker.present();
  }
}
