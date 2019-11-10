import { Component, OnInit } from '@angular/core';
import { MemoryService } from '../services/memory.service';
import { Memory } from '../models';

@Component({
  selector: 'app-view',
  templateUrl: './view.page.html',
  styleUrls: ['./view.page.scss'],
})
export class ViewPage implements OnInit {
  memories: Memory[]
  constructor(private memoryService: MemoryService) {

   }

  ngOnInit() {
     this.memoryService.getMemories().then(data => {
      this.memories = data
      console.log(data)
    })
  }

  

}
